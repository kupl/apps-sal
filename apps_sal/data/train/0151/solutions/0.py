class Solution:
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        def length_requirement(password):
            length = len(password)
            if length < 6:
                return 6 - length
            elif length > 20:
                return 20 - length
            else:
                return 0

        def category_requirement(password):
            string = set(password)
            lowercase = set('qwertyuiopasdfghjklzxcvbnm')
            uppercase = set('QWERTYUIOPASDFGHJKLZXCVBNM')
            digit = set('1234567890')
            condition = [lowercase, uppercase, digit]
            missing = 0
            for s in condition:
                if not s & string:
                    missing += 1
            return missing

        def repeat_requirement(password):
            count = 1
            repeat = None
            weak_pair = []
            for c in password:
                if c == repeat:
                    count += 1
                else:
                    if count >= 3:
                        weak_pair.append([repeat, count])
                    count = 1
                    repeat = c
            if count >= 3:
                weak_pair.append([repeat, count])
            change = 0
            one = 0
            two = 0
            for _, length in weak_pair:
                change += length // 3
                if length % 3 == 0:
                    one += 1
                elif length % 3 == 1:
                    two += 1
            return change, one, two

        def minimum_change(password):
            print(password, end=' ')
            length = length_requirement(password)
            category = category_requirement(password)
            repeat, one, two = repeat_requirement(password)
            print(length, category, repeat, one, two, end=' * ')

            if length >= 0:
                return max(length, category, repeat)
            else:
                delete = - length
                repeat -= min(delete, one)
                repeat -= min(max(delete - one, 0), two * 2) // 2
                repeat -= max(delete - one - 2 * two, 0) // 3
                return delete + max(category, repeat)

        return minimum_change(s)
