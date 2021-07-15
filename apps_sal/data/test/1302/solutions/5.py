
def k_beautiful(n, k):
    if n <= k:
        return [-1]
    else:
        beautiful = [i for i in range(1, n+1)]
    
    # make them not beauftiful
    left = n- k - 1
    if left % 2 == 0:
        for i in range(k+1, n, 2):
            beautiful[i], beautiful[i+1] = beautiful[i+1], beautiful[i] 
    else:
        for i in range(k+1, n-1, 2):
            beautiful[i], beautiful[i+1] = beautiful[i+1], beautiful[i]
        beautiful[0], beautiful[-1] = beautiful[-1], beautiful[0]
        
        
    return beautiful

def print_l(l):
    string = ""
    for item in l:
        string += str(item) + " "
    if len(string) > 1:
        string = string[0:len(string) - 1]
    print(string)
    
        
def main():
    i = input().split()
    n = int(i[0])
    k = int(i[1])
    print_l(k_beautiful(n, k))

main()

