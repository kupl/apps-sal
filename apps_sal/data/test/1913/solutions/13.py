def main():
    n = int(input())
    arr = [str(x) for x in input().split()]
    zero = 0
    x = None
    q = False
    for i in range(n):
        a = arr[i].count("1")
        b = arr[i].count("0")        
        if arr[i] == "0":
            q = True
        if a == 1 and a + b == len(arr[i]):
            zero += len(arr[i]) - 1
        else:
            x = arr[i]
    if q:
        print(0)
    else:
        if x is not None:
            print(x, end="")
        else:
            print("1", end="")
        print("0" * zero)
    
    
main()
