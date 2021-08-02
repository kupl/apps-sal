ans = []
X = int(input())
for i in range(1, 50):
    for j in range(2, 20):
        if (i ** j) <= X:
            ans.append(i**j)
print(max(ans))
