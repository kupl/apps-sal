def main():
    s = input()
    res = 0
    for elem in s:
        if int(elem) % 4 == 0:
            res += 1
    for i in range(len(s) - 1):
        if int(s[i:i + 2]) % 4 == 0:
            res += i + 1
    print(res)
    
main()
