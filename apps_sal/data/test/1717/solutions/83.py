def find_lcm(num1, num2):
    if num1 > num2:
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while rem != 0:
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm


n = int(input())
arr = [i for i in range(1, n + 1)]
lcm = find_lcm(arr[0], arr[1])
i = 2
while i < n:
    lcm = find_lcm(lcm, arr[i])
    i += 1
print(lcm + 1)
