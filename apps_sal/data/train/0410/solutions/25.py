class Solution:
    def calc(self, num):
        count = 0
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            count += 1
        return count

    def getKth(self, lo: int, hi: int, k: int) -> int:
        counts = []
        keys = [i for i in range(lo, hi + 1)]
        dict = {}

        for i in range(lo, hi + 1):
            ans = self.calc(i)
            counts.append(ans)

        for key in keys:
            for count in counts:
                dict[key] = count
                counts.remove(count)
                break

        dict = {k: v for k, v in sorted(list(dict.items()), key=lambda item: item[1])}
        final = [key for key in list(dict.keys())]
        return final[k - 1]
