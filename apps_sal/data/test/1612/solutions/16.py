def s():
    n = int(input())
    a = [set(list(map(int, input().split()))[1:])for _ in range(n)]
    res = 0
    print(*['YES'if sum(i.issubset(j)for i in a) == 1 else 'NO' for j in a], sep='\n')


s()
