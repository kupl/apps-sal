n = int(input())
arr1 = []
arr2 = []
for _ in range(n):
    arr1 += [input()]
for _ in range(n):
    arr2 += [input()]

for word in arr1:
    if word in arr2:
        arr2.remove(word)
print(len(arr2))
