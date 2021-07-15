def main():
    input()
    numbers = list(map(int, input().split()))


    if len(numbers) < 2 or (len(numbers) == 2 and numbers[0] == numbers[1]):
        print(-1)
        return

    print(1)
    print(numbers.index(min(numbers)) + 1)
    
main()
