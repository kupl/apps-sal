def main():
    s = input()
    
    if s[-1] != "s":
        result = s +"s"
    else:
        result = s + "es"
    
    print(result)


main()
