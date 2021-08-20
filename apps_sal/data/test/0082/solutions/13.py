(n, k) = map(int, input().split())
marks = list(map(int, input().split()))
summa = sum(marks)
nums = len(marks)
result = summa / nums
howmany = 0
while result < k - 0.5:
    summa += k
    nums += 1
    result = summa / nums
    howmany += 1
print(howmany)
