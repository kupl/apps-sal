import time
import string


class Profiler(object):

    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print('Elapsed time: {:.3f} sec'.format(time.time() - self._startTime))


k = int(input())
s = input()
m = {}
for el in string.ascii_lowercase:
    m[el] = 0
if len(set(s)) < k:
    print('NO')
else:
    i = 0
    t = []
    while i < len(s):
        if k == 1:
            t.append(s[i:])
            break
        if m[s[i]] == 0:
            m[s[i]] = 1
            tmp = s[i]
            i += 1
            while i < len(s) and m[s[i]]:
                tmp += s[i]
                i += 1
            t.append(tmp)
            k -= 1
        else:
            i += 1
    print('YES')
    for el in t:
        print(el)
'\nfin = open("input.txt")\nfout = open("output.txt", "w")\n\nn = int(fin.readline())\ncases = list()\n\nfor i in range(n):\n    fin.readline()\n    cases.append(list(fin.readline().split()))\n\nfor i in range(1, len(cases)+1):\n    cur_min = 1001\n    added_min = 0\n    lst = list(map(int, cases[i-1]))\n    while max(lst) > 1:\n        mmax = max(lst)\n        if cur_min > mmax + added_min:\n            cur_min = mmax + added_min\n        count_max = lst.count(mmax)\n        tmp_lst = list()\n        for sym in lst:\n            if sym is not mmax:\n                tmp_lst.append(sym)\n            else:\n                if sym % 2 is 0:\n                    tmp_lst.append(sym//2)\n                    tmp_lst.append(sym//2)\n                else:\n                    tmp_lst.append(sym//2)\n                    tmp_lst.append(sym//2 + 1)\n        added_min += count_max\n        lst = tmp_lst.copy()\n\n\n\n    fout.write("Case #" + i.__str__() + ": " + cur_min.__str__() + "\n")\nfin.close()\nfout.close()\n'
