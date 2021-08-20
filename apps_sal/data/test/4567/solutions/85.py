n = int(input())
s = list((int(input()) for _ in range(n)))
s.sort()
if all((num % 10 == 0 for num in s)):
    print(0)
elif sum(s) % 10 == 0:
    for num in s:
        if num % 10 != 0:
            print(sum(s) - num)
            break
else:
    print(sum(s))
