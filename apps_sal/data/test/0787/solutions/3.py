import time
import string


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


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

'''
fin = open("input.txt")
fout = open("output.txt", "w")

n = int(fin.readline())
cases = list()

for i in range(n):
    fin.readline()
    cases.append(list(fin.readline().split()))

for i in range(1, len(cases)+1):
    cur_min = 1001
    added_min = 0
    lst = list(map(int, cases[i-1]))
    while max(lst) > 1:
        mmax = max(lst)
        if cur_min > mmax + added_min:
            cur_min = mmax + added_min
        count_max = lst.count(mmax)
        tmp_lst = list()
        for sym in lst:
            if sym is not mmax:
                tmp_lst.append(sym)
            else:
                if sym % 2 is 0:
                    tmp_lst.append(sym//2)
                    tmp_lst.append(sym//2)
                else:
                    tmp_lst.append(sym//2)
                    tmp_lst.append(sym//2 + 1)
        added_min += count_max
        lst = tmp_lst.copy()



    fout.write("Case 
fin.close()
fout.close()
'''
