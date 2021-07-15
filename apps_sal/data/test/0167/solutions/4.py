a = input()
b = input()

prefix = [-1] * len(b)
postfix = [-1] * len(b)

prefix[0] = a.find(b[0])
postfix[len(b) - 1] = a.rfind(b[len(b) - 1])

for i in range(1, len(b)):
    prefix[i] = a.find(b[i], prefix[i - 1] + 1)
    if prefix[i] == -1:
        break

for i in range(len(b) - 2, -1, -1):
    postfix[i] = a.rfind(b[i], 0, postfix[i+1])
    if postfix[i] == -1:
        break

best_left = -1
best_right = len(b)

left = -1
while left + 1 < len(b) and prefix[left + 1] != -1:
    left += 1

if left > -1:
    best_left = left
    best_right = len(b)

right = len(b)
while right - 1 >= 0 and postfix[right - 1] != -1:
    right -= 1

if right < len(b) and right + 1 < best_right - best_left:
    best_left = -1
    best_right = right

left = 0
right = len(b)

while left < right and postfix[right - 1] != -1 and postfix[right - 1] > prefix[left]:
    right -= 1

while prefix[left] != -1 and left < right < len(b):
    while right < len(b) and postfix[right] <= prefix[left]:
        right += 1

    if right >= len(b):
        break

    if right - left < best_right - best_left:
        best_left = left
        best_right = right

    left += 1

    if left == right:
        right += 1

res = b[:best_left + 1] + b[best_right:]
if res == "":
    print("-")
else:
    print(res)

