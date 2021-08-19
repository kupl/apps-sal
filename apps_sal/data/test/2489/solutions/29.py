N = int(input())
A = list(map(int, input().split()))
A.sort()
minNum = A[0]
maxNum = A[N - 1]
countList = [0] * (10**6 + 1)
answer = 0

# Aにnがm個あるときcountList[n] = m
for i in A:
    countList[i] += 1

for j in range(minNum, maxNum + 1):
    # Aにjが含まれていれば、jの倍数をすべてcountListから除外
    # jの倍数pはjで割り切れるので除外可能
    # pの倍数qはjでも割り切れるのでjの時の処理によって除外される
    if countList[j] > 0:
        for k in range(2 * j, 10**6 + 1, j):
            countList[k] = 0
    # jが2個以上ある場合にはそれを正解としてカウントしない
    if countList[j] == 1:
        answer += 1

print(answer)
