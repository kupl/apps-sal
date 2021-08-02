input(); a = {j: i + 1 for i, j in enumerate(map(int, input().split()))}
print(*[j for i, j in sorted(a.items(), key=lambda x:x[0])])
