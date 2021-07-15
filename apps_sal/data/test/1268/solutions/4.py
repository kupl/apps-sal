def main():
    read = lambda: tuple(map(int, input().split()))
    n = read()[0]
    a = read()
    b = sorted(read())
    
    sm = sum(a)
    
    if sm <= b[-1] + b[-2]:
        print("YES")
    else:
        print("NO")
   
main()

