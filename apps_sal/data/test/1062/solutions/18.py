import time


class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print("Elapsed time: {:.3f} sec".format(time.time() - self._startTime))


n = int(input())
a = input()
b = input()
indexes = list()
d = {}
f1 = False
f2 = False
df = 0
i1 = 0
i2 = 0
for i in range(n):
    if a[i] != b[i]:
        df += 1
        indexes.append(i)
        d[b[i]] = i
for i in indexes:
    if a[i] in d:
        f1 = True
        j = d[a[i]]
        i1 = i + 1
        i2 = j + 1
        if a[j] == b[i]:
            f2 = True
            break
if f2:
    print(str(df - 2))
    print(i1.__str__() + ' ' + i2.__str__())
elif f1:
    print(str(df - 1))
    print(i1.__str__() + ' ' + i2.__str__())
else:
    print(str(df))
    print('-1 -1')
