__author__ = "Ryabchun Vladimir"


class Stack:
    """
    This is a stack class. There is 5 Procedures we can do with stack:
    1. Push - we add one element at the end of the stack
    2. Pop - we remove last element from the stack and return it
    3. Last - We return last element but don't remove it
    4. len() - returns the length of stack(we don't use len() because it's too
    slow).
    5. Clear - remove all elements from stack
    """

    def __init__(self, element=None):
        """
        self.length - length of the stack. When we append an element we increase it(length) by 1
        __stack - this is our stack. Because we can't get any elements from the stack except the last one
        we have to keep our stack as a private variable(we can receive any element - foo = Stack(); foo.stack[0] = 0,
        but we mustn't do it).
        :param element: Can be any type
        """
        self.length = 0
        if element is None:
            self.__stack = []
        else:
            self.__stack = []
            for el in element:
                self.__stack.append(el)
                self.length += 1

    def push(self, element):
        """
        This function adds an element at the end of the stack.
        When we append an element we increase self.length by 1.
        :param element: Can be any type
        :return: NoneType
        """
        self.__stack.append(element)
        self.length += 1

    def pop(self):
        """
        This function removes an element from the end of the stack and
        returns it's value.
        When we append an element we decrease self.length by 1.
        :return: Last element from the stack
        """
        if self.length == 0:
            raise IndexError("Stack is empty")
        else:
            self.length -= 1
            return self.__stack.pop()

    def last(self):
        """
        This function just returns an element from the end of the stack
        but it doesn't remove it.
        :return: Last element from the stack
        """
        if self.length == 0:
            raise IndexError("Stack is empty")
        else:
            return self.__stack[-1]

    def __len__(self):
        """
        This function returns the length of the stack.
        :return: self.length(int)
        """
        return self.length

    def clear(self):
        """
        Clears the stack.
        :return: NoneType
        """
        self.__stack = []


n = int(input())
snekovik = Stack()
wrong_snaks = set()
the_biggest_snek = n
sneks = list(map(int, input().split()))
for i in sneks:
    printing = []
    if i == the_biggest_snek:
        snekovik.push(i)
        printing.append(i)
        the_biggest_snek -= 1
        while the_biggest_snek in wrong_snaks:
            snekovik.push(the_biggest_snek)
            wrong_snaks.remove(the_biggest_snek)
            printing.append(the_biggest_snek)
            the_biggest_snek -= 1
    else:
        wrong_snaks.add(i)
    print(*printing)
