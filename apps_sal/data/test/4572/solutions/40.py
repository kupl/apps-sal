def main():
    s=input()
    for x in range(ord('a'), ord('z')+1):
        c=chr(x)
        if c in s:
            continue
        else:
            print(c)
            return
    print('None')
main()
