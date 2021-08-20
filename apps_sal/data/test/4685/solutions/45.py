ABC = [int(_) for _ in input().split()]
K = int(input())
ABC = sorted(ABC)
ret = ABC[2]
for i in range(K):
    ret = ret * 2
ret += sum(ABC[:2])
print(ret)
