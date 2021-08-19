from sys import stdin
(N, K) = map(int, stdin.readline().split())
charArr = list(stdin.readline().strip())
bad = 0
front = 0
front2 = 0
back = len(charArr)
answer = K
while front < back:
    if charArr[front] != 'a':
        bad += 1
    if bad > K:
        while front2 <= front and charArr[front2] == 'a':
            front2 += 1
        bad -= 1
        front2 += 1
    answer = max(answer, front - front2 + 1)
    front += 1
bad = 0
front = 0
front2 = 0
back = len(charArr)
while front < back:
    if charArr[front] != 'b':
        bad += 1
    if bad > K:
        while front2 <= front and charArr[front2] == 'b':
            front2 += 1
        bad -= 1
        front2 += 1
    answer = max(answer, front - front2 + 1)
    front += 1
print(answer)
