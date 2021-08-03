print("None" if len(s := (set(list("abcdefghijklmnopqrstuvwxyz")) - set(input()))) == 0 else sorted(list(s))[0])
