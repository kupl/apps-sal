n = int(input())
words = [input() for _ in range(n)]
abc = list('qwertyuiopasdfghjklzxcvbnm')
ans = 0
for i in range(len(abc)):
    for j in range(i + 1, len(abc)):
        preAns = 0
        for word in words:
            canAdd = True
            for char in word:
                if char != abc[i] and char != abc[j]:
                    canAdd = False
                    break
            if canAdd:
                preAns += len(word)
        ans = max(ans, preAns)
print(ans)
