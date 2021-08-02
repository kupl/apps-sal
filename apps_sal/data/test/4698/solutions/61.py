input(); t = [*map(int, input().split())]; T = sum(t)
print(*[T - t[i - 1] + j for i, j in [[*map(int, input().split())] for _ in range(int(input()))]], sep='\n')
