n = int(input())
p = list((int(input()) for _ in range(n)))
p.append(p.pop(p.index(max(p))) // 2)
print(sum(p))
