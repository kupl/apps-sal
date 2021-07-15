# array de indices em ordem crescente
# quantos 2**b precisa para 2**v-1 (soma de sequencia)

import math

def main():
    n = int(input())
    a = input().split()
    a = [int(x) for x in a]
    
    p = 0
    carry = 0
    ok = 0
    while p<n:
        count = carry
        atual = a[p]
        while p<n and a[p] == atual:
            count += 1
            p += 1 
        if count%2 == 1:
            ok += 1
        carry = count//2 
        if p<n:       
            proximo = a[p]
        else:
            proximo = atual-1    
        while carry!= 0 and proximo!= atual+1:
            if carry%2 == 1:
                ok += 1
            carry = carry//2         
            atual += 1
    print(atual-ok+1)    

main()
