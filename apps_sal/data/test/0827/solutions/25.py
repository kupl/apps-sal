"""
prefix: "0", "10"
sufix:  "1", "11"
"""
def main():
    ans = 10**10 + 1
    N = int(input())
    T = input()

    if T == '1':
        print((2*10**10))
        return

    if T and T[0] == "0":
        T = T[1:]
        ans -= 1
    elif 2 <= len(T) and T[0:2] == '10':
        T = T[2:]
        ans -= 1
    
    if 2 <= len(T) and T[-2:] == '11':
        T = T[:-2]
        ans -= 1
    elif T and T[-1] == "1":
        T = T[:-1]
        ans -= 1

    for i in range(0,len(T),3):
        if not T[i:i+3] == '110':
            print((0))
            return
    print((ans - len(T)//3))
        
main()
    


