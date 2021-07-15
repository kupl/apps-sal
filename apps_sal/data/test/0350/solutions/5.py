N = int(input())
letters = list(map(int, input().split()))
letters.sort()
lennow = 0
for i in range(len(letters) - 2, -1, -1):
    letters[i] = max(0, min(letters[i + 1] - 1, letters[i]))
print(sum(letters))
