def main():
    n, m = map(int, input().split())
    mas = list(map(int, input().split()))
    
    remains = set()
    
    for i in range(n):
        for_add = set()
        for e in remains:
            if (e + mas[i]) % m == 0:
                return True
            else:
                for_add.add((e + mas[i]) % m)
        
        if mas[i] % m == 0:
            return True
        else:
            for_add.add(mas[i])
            
        remains |= for_add

if main():
    print("YES")
else:
    print("NO")
