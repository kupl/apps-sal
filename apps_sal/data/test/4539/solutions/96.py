def harshad(n):
    if n % sum(map(int, list(str(n)))) == 0:
        return True
    else:
        return False


N = int(input())
print('Yes' if harshad(N) else 'No')
