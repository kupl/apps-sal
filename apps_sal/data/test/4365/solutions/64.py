def main():
    K = int(input())
    oddnum = K // 2
    evennum = K // 2 + K % 2
    ans = oddnum * evennum
    return ans


print((main()))
