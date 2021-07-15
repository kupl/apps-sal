def main():
    n = int(input())
    our = [input() for i in range(n)]
    made = set()
    while our:
        c = our[-1]
        if c not in made:
            made.add(c)
            print(c)
        our.pop()
    
main()
