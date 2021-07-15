def caps(s):
    first_bit = s[0].capitalize()
    
    return first_bit + s[1:]


def main():
    first_word = input()
    print(caps(first_word))
    
        
    
main()   


