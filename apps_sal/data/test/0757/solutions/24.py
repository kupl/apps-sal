n, m, k = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort(reverse=True)
# l.reverse()
# print(l)
if m <= k:
    print(0)
    quit()
for ii, c in enumerate(l):
    k += c - 1
    # print(k)
    if k >= m:
        print('{}'.format(ii + 1))
        quit()
print(-1)
