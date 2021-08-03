__author__ = 'trunghieu11 - vuondenthanhcong11@gmail.com'

# ---------- Actual Code ----------

count, a, b = list(map(int, input().split()))
areaNeed = 6 * count

if a * b >= areaNeed:
    print(a * b)
    print(a, b)
    return

isSwap = False
if a > b:
    a, b = b, a
    isSwap = True

answerArea = 10**10
answerA = -1
answerB = -1

for i in range(a, int(areaNeed ** 0.5) + 1):
    curB = (areaNeed + i - 1) // i
    if curB >= b:
        curArea = i * curB
        if curArea < answerArea:
            answerArea = curArea
            answerA = i
            answerB = curB

if isSwap:
    answerA, answerB = answerB, answerA

print(answerArea)
print(answerA, answerB)

# ---------- My Tools -------------
