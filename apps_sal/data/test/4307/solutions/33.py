def make_divisors(n: int) -> list:
    return_list = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            return_list.append(i)
            if i != n // i:
                return_list.append(n//i)

    return return_list
N = int(input())
cnt = 0
for i in range(1,N+1,2):
    if len(make_divisors(i)) == 8:
        cnt += 1
print(cnt)
