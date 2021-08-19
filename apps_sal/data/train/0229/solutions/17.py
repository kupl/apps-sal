class Solution:

    def canReorderDoubled(self, arr):
        arr.sort()
        negl = [x for x in arr if x < 0][::-1]
        posl = [x for x in arr if x >= 0]
        cnt = {}
        for x in arr:
            if x not in cnt:
                cnt[x] = 1
            else:
                cnt[x] = cnt[x] + 1
        while True:
            x = None
            if negl != []:
                x = negl.pop(0)
            elif posl != []:
                x = posl.pop(0)
            else:
                break
            if cnt[x] == 0:
                continue
            y = x * 2
            if y not in cnt:
                return False
            elif cnt[y] > 0 and cnt[x] > 0:
                cnt[y] = cnt[y] - 1
                cnt[x] = cnt[x] - 1
            else:
                return False
        return True
