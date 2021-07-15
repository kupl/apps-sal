def main():
      a, b = list(map(int, input().split()))
      count = 0
      mx = max(a,b)
      while  a:
        if a < b:
            a,b=b,a
        less = a // b
        count += less
        a -= b*less
      print(count)
def __starting_point():
    main()

__starting_point()
