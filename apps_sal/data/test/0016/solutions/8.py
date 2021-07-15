def main():
    a, b, c, d = (int(input()) for i in range(4))
    if (a == d == 0):
        if (c == 0):
            print(1)
        else:
            print(0)
    elif (a == d):
        print(1)
    else:
        print(0)
 
 
main()

