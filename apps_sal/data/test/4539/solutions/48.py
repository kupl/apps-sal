def main():
    N = int(input())
    X = N
    sum = 0
    while True:
        amari = N % 10
        sum += amari
        N //= 10
        if N == 0:
            break

    if X % sum == 0:
        return 'Yes'
    else:
        return 'No'


print((main()))
