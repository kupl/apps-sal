a, b = map(int, input().split())

for i in range(2, 400):
    if (10**(len(str(b))) * a + b) == i**2:
        ans = 'Yes'
        break
    else:
        ans = 'No'
print(ans)
