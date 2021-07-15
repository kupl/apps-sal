num = input();

for i in reversed(num):
    n = int(i);
    if n >= 5:
        print("-O|", end="");
        n = n-5;
    else:
        print("O-|", end="");
    
    if n == 4:
        print("OOOO-");
    elif n == 3:
        print("OOO-O");
    elif n == 2:
        print("OO-OO");
    elif n == 1:
        print("O-OOO");
    else:
        print("-OOOO");
        
        

