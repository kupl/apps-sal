n = int(input())
students = [[], [], []]
for i, j in enumerate(map(int, input().split())):
    students[j - 1].append(i + 1)
ans = min(len(students[i]) for i in range(3))
print(ans)
if ans:
    for i in range(ans):
        print(*[students[j][i] for j in range(3)])
