def list_from_input():
    return list(map(int, input().split()))


class Mouse:
    def __init__(self, price, type):
        self.type = type
        self.price = price

    @classmethod
    def from_input(cls):
        mouse_data = input().split()
        price = int(mouse_data[0])
        type = mouse_data[1][0]
        return Mouse(price, type)


def main():
    usb_pc, ps_pc, both_pc = list_from_input()
    mouses_count = int(input())

    mouses = []
    for i in range(mouses_count):
        mouses.append(Mouse.from_input())

    mouses.sort(key=lambda mouse: mouse.price)
    purchase_amount = 0
    pc_with_mouses = 0
    for mouse in mouses:
        if mouse.type is 'U' and usb_pc > 0:
            usb_pc -= 1
            purchase_amount += mouse.price
            pc_with_mouses += 1
        elif mouse.type is 'P' and ps_pc > 0:
            ps_pc -= 1
            purchase_amount += mouse.price
            pc_with_mouses += 1
        elif both_pc > 0:
            both_pc -= 1
            purchase_amount += mouse.price
            pc_with_mouses += 1

    print(pc_with_mouses, purchase_amount)


main()
