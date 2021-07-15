n = int(input())
answer = "NO"
for _ in range(n):
    s = str(input())
    arr = s.split()
    a = int(arr[1])
    b = int(arr[2])

    if a >= 2400 and b > a:
        answer = "YES"

print(answer)
