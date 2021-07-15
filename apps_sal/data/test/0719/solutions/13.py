aa = set()
for i1 in range(0, 10):
    for i2 in range(min(11 - i1, 10)):
        for i3 in range(min(11 - i1 - i2, 10)):
            for i4 in range(min(11 - i1 - i2 - i3, 10)):
                for i5 in range(min(11 - i1 - i2 - i3 - i4, 10)):
                    for i6 in range(min(11 - i1 - i2 - i3 - i4 - i5, 10)):
                        for i7 in range(min(11 - i1 - i2 - i3 - i4 - i5 - i6, 10)):
                            a = [i1, i2, i3, i4, i5, i6, i7, 10 - i1 - i2 - i3 - i4 - i5 - i6 - i7]
                            t = sum([10 ** i * a[i] for i in range(8)])
                            aa.add(t)
ans = list(aa)
ans.sort()
k = int(input())
print(ans[k - 1])
