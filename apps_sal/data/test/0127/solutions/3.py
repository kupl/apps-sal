l = input().strip().split()
n , f = int(l[0]) , int(l[1])

lst = []
base = []
for i in range(n):
    l = input().split()
    k , l = int(l[0]) , int(l[1])
    base.append(min(l,k))
    lst.append(max(0, min(k, l - k)))
    # print('>>',base[-1], lst[-1])
lst = sorted(lst, reverse=True)
print(sum(lst[:f]) + sum(base))
