def read(): return list(map(int, input().split()))


n = int(input())
p = list(read())
Max = max(p)
ind = p.index(Max) + 1
p.remove(Max)
Max2 = max(p)
print(ind, Max2)
