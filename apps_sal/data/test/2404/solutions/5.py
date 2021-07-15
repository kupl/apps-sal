import bisect, collections
 
 
 
def solution():
    
    n = int(input().strip())

    for i in range(2, n):
        if n % i == 0:
            print(str(i)+str(n//i))
            break
    


    

def main():    
    # T = int(input().strip())
    for _ in range(1):
        solution()

def __starting_point():
    main()
__starting_point()
