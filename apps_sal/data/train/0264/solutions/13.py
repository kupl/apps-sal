class Solution:

    def maxLength(self, arr: List[str]) -> int:
        filtered = []
        for string in arr:
            seen = {}
            good = True
            for letter in string:
                if letter in seen:
                    good = False
                else:
                    seen[letter] = True
            if good:
                filtered.append(string)
        self.memo = {}
        print(filtered)
        return self.getLength(0, filtered, {})

    def getLength(self, current, arr, used):
        if not arr:
            return current
        if tuple(arr) in self.memo:
            return self.memo[tuple(arr)]
        maxi = current
        for index in range(len(arr)):
            string = arr[index]
            possible = True
            for char in string:
                if char in used:
                    possible = False
            if not possible:
                continue
            for char in string:
                used[char] = True
            result = self.getLength(current + len(string), arr[:index] + arr[index + 1:], used)
            if result > maxi:
                maxi = result
            for char in string:
                del used[char]
        self.memo[tuple(arr)] = maxi
        return maxi
