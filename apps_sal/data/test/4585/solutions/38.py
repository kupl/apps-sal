def get_index(n):
    i = 1
    while True:
        if n <= piramid(i):
            return i - 1
        i += 1


def piramid(n):
    return n * (n + 1) // 2


n = int(input())
index = get_index(n)

print(index + 1)
